## GR5526(5)-构建Lvgl 应用初步 

[TOC]


### 1. 前言

LVGL(Little and Versatile Graphics Library)是一个在嵌入式领域广泛使用的GUI框架，其最主要的特性就是自带一套完整且好用的控件/样式库和渲染方法，其简单易懂的API设计让几乎任何一个有GUI开发经验的人都能快速上手，即使没有相关经验学起来也相对容易。

而GR5526这样一颗可以说是为了刷屏而生的BLE SoC，其官方SDK中也有基于LVGL的刷屏演示工程。本系列将从GR5526 SDK V1.0.1中的graphics_lvgl_831_gpu_demo演示工程出发，从如何使用LVGL到完整理解LVGL框架进行讲解。

### 2.下载样例工程尝鲜

由于SDK包中已经提供了现成的Example工程，所以我们先把这个工程下载下去看看效果。

使用Keil打开位于projects/peripheral/graphics/graphics_lvgl_831_gpu_demo/Keil_5/graphics_lvgl_831_gpu_demo.uvprojx的工程文件，就能看到官方提供的Example工程：

![在这里插入图片描述](https://img-blog.csdnimg.cn/06792e57bf134066b0d55b0699d269e5.png)


可以看到工程内容相当的复杂，不过不要紧，我们先把固件下下去看看效果，之后再来慢慢啃这块硬骨头。点击Build按钮或者按快捷键F7进行编译。初次编译可能会需要比较长的时间。
![在这里插入图片描述](https://img-blog.csdnimg.cn/53bd70a311994745b54f70b50583c54d.png)


编译完成后点击Download按钮或者按快捷键F8进行下载，等待固件下载完成，就能看到效果了：
![在这里插入图片描述](https://img-blog.csdnimg.cn/9793a3b793894005ba3a88e5567fb47a.png)



可以看到，屏幕是花的。因为Example引用的图片资源和固件并没有存放在同一个位置，图片资源要另外下载，需要使用GProgrammer工具来做。打开GProgrammer之后，找到GR5526VGBIP的选项，点击OK：
![在这里插入图片描述](https://img-blog.csdnimg.cn/6baacaf00b38483fa79f3a078e3fc73e.png)



之后右边会有一个弹出窗口，点击Connect连接开发板：
![在这里插入图片描述](https://img-blog.csdnimg.cn/5e3e89121af343febae5765ad0dc4e2e.png)



等待开发板连上之后，在左边那一排图标里选择第二个"Flash"，进入资源烧录界面：
![在这里插入图片描述](https://img-blog.csdnimg.cn/c4a40a5d7a214d998eeb066dc7b546bf.png)



选择External Flash，点击Config，会弹出来一个对话框，要求选择存储资源的Flash对应的接口。对于GR5526 SK开发板来讲，选择QSPI0，其余的保持默认配置，点击Apply。片刻之后可以看到GProgrammer已经识别了板子上的XTX25Q64B 8M Flash。
![在这里插入图片描述](https://img-blog.csdnimg.cn/6dadb92637964bfb92d54df4ea178d1c.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/225f2b44732747ea80481b50055abace.png)





在下面的Download Data区域，点右边的文件夹找到图片资源文件。图片资源文件在Example工程的Image_Resource文件夹下有一个0x0000_2023-06-06_17-38-37.bin，选择这个文件，下载地址填写0，点击Download开始下载图片资源。由于这个资源有5M多，所以下载应该会花上一些时间。
![在这里插入图片描述](https://img-blog.csdnimg.cn/d8752757e72a4f4e9b3d92461b3ba06c.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/042043ccd70a4504af92c9f80759d183.png)




下载完成后，按一下板子上的Reset按钮，让固件重新跑起来，再看效果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/42e3b91e71744ad9b9a2feb2f84dd19c.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/3dd34ba69dd3447aa7d29e9e343d6c3d.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/0c67b5c55612440eafa3afe2d09bfbb6.png)






（卡顿是GIF的问题，实际效果很流畅）

可以看到一个类似智能手表的界面已经出来了，滑一滑，点一点，看起来还是做了挺多界面的。而且在滑动过程中还有一些3D动画效果，看起来挺酷炫的。

### 3. 编写第一个LVGL界面

#### 3.1 寻找GUI入口点

Example看完了，现在回归正题，来制作我们自己的LVGL界面。在着手编写代码之前，我们得先知道我们自己的代码要往哪儿放。遇事不决从main()函数开始看，先打开main.c，找到main()函数：
```c
static void vStartTasks(void *arg)
{
	lv_user_task_create();
	osal_task_delete(NULL);
}

int main(void)
{
	app_graphics_adjust_dcore_policy();                             /*<Should call this firstly if using graphics modules */
	SetSerialClock(SERIAL_N96M_CLK);
	app_periph_init();                                              /*<Init user periph .*/
	// Initialize ble stack.
	ble_stack_init(ble_evt_handler, &heaps_table);
	osal_task_create("create_task", vStartTasks, 1024, 0, NULL);
	osal_task_start();
	for (;;);                                                       /*< Never perform here */
}
```

对RTOS熟悉的朋友可能一眼就看出来了，虽然用osal_task_xxx包了一层，但实际这个工程是基于FreeRTOS构建的。关于操作系统的内容这里不展开说，因为都是模板工程预先配置好的，我们直接用就行了，不用太关心细节。

可以看到在main()里面创建了一个vTaskStart任务，顺着往上看，在vTaskStart里面又执行了一个叫lv_user_task_create()的函数，从字面意思来理解，这里肯定就是GUI线程的入口了，跟进去看一看：
```c
void lv_user_task_create(void)
{
	osal_task_create("task_indev", app_indev_read_task, TASK_SIZE_TOUCHPAD_READ, TASK_PRIO_TOUCHPAD_READ, &g_task_handle.indev_handle);
	osal_task_create("task_gui",   app_gui_render_task, TASK_SIZE_GUI_RENDER,    TASK_PRIO_GUI_RENDER,    &g_task_handle.gui_handle);
	extern void lv_gui_evt_task_startup(void);
	lv_gui_evt_task_startup();
}
```

可以看出，这个函数创建两个任务，一个用来处理GUI，另一个用来处理输入设备。我们顺着处理GUI那个任务继续跟进去：

```c
void app_gui_render_task(void *p_arg)
{
	uint32_t delayTime = 0;
	mock_data_init_pre_gui();
	lvgl_env_init();
	lv_layout_router_init();
	mock_data_init_post_gui();
	while(1){
		delayTime = lv_task_handler();
		if(SYS_STATE_SLEEP != sys_state_get()) {
			//osal_task_delay(delayTime);
			osal_sema_take(s_gui_refresh_sem, delayTime);
		} else {
			osal_sema_take(s_gui_refresh_sem, OSAL_MAX_DELAY);
		}
	}
}
```

看来这里就是我们要找的入口点了。其中mock_data_init_pre_gui()、lv_layout_router_init()和mock_data_init_post_gui()都是演示Demo相关的内容，只有lvgl_env_init()是真正初始化LVGL的部分。所以我们直接把无关的内容删掉以便于等下添加我们自己的界面：

```c
void app_gui_render_task(void *p_arg)
{
	uint32_t delayTime = 0;
	lvgl_env_init();
	/**
	My Code Here
	**/
	while(1){
		delayTime = lv_task_handler();
		if(SYS_STATE_SLEEP != sys_state_get()) {
			//osal_task_delay(delayTime);
			osal_sema_take(s_gui_refresh_sem, delayTime);
		} else {
			osal_sema_take(s_gui_refresh_sem, OSAL_MAX_DELAY);
		}
	}
}
```

#### 3.2 编写一个LVGL界面

现在我们来编写一个简单的LVGL界面，随便找个地方新建一个my_layout.c，加入到Keil工程并写入以下代码：

```c
#include "lvgl.h"

void my_first_lvgl_layout(void)
{
	lv_obj_t *screen = lv_obj_create(NULL);
	lv_obj_set_style_bg_color(screen, lv_color_black(), LV_PART_MAIN);
	lv_obj_set_style_bg_opa(screen, LV_OPA_COVER, LV_PART_MAIN);
	lv_obj_t *label = lv_label_create(screen);
	lv_label_set_text(label, "Hello World!");
	lv_obj_center(label);
	lv_scr_load(screen);
}
```

代码的内容非常简单，从上到下依次是：

创建一个窗口
将窗口背景色设置为黑色
将窗口背景色设置为不透明
在窗口中创建一个label（即标签）控件
将label控件的内容设置为"Hello World!"
将label控件居中
加载刚刚创建的窗口
在细讲每个函数的用法之前，我们先让这段代码跑起来。回到刚刚lv_user_task.c中的GUI线程，我们在LVGL初始化完成之后，调用我们自己的页面创建函数，像这样：

```c
 void app_gui_render_task(void *p_arg)
{
	uint32_t delayTime = 0;
	lvgl_env_init();
	extern void my_first_lvgl_layout(void);
	my_first_lvgl_layout();
	while(1){
		delayTime = lv_task_handler();
		if(SYS_STATE_SLEEP != sys_state_get()) {
			//osal_task_delay(delayTime);
			osal_sema_take(s_gui_refresh_sem, delayTime);
		} else {
			osal_sema_take(s_gui_refresh_sem, OSAL_MAX_DELAY);
		}
	}
}
```

比较正统的做法应该是使用一个头文件来暴露所有的公开接口，这里我就偷个懒，直接extern过来调用。添加完代码之后，直接编译，下载，来看看效果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/2060778b76d94df9b733328d351ad745.png)


可以看到在屏幕中间出现了"Hello World"字样，正是我们刚刚创建的窗口。下面将基于刚才创建的窗口对LVGL的使用做一个基本的介绍。

### 4. LVGL基本概念

针对上面my_first_lvgl_layout中出现的概念，这里做一个简单的讲解。

#### 4.1 LVGL对象

使用LVGL构建基本界面的时候，最基本的单位是object。object本质上还是个结构体，里面存储了一系列最基本的确定控件属性的参数，大体可以分为以下几类：

- 对象树关系类：例如父对象，子对象，子对象数量。
- 样式类：例如样式列表，样式数量。
- 几何类：对象位置，绘制区域，布局参数等等。
- 状态类：对象状态，对象功能Flag等等。
- 滚动类：滚动位置，滚动方向，滚动吸附等等。
- 事件响应类：事件响应函数，响应事件类型等等。

其余所有的控件都会通过将lv_obj_t结构体放在第一个位置的方法来“继承”这个结构体，达到任何衍生控件都能拥有同样的基础属性的效果。

LVGL依照对象树的结构来管理所有的object。一个object有一个或零个父对象，一个object可以有若干个子对象：

![在这里插入图片描述](https://img-blog.csdnimg.cn/16184235b8724fd79a836ffca3f23686.png)

在对象树中，一个父对象可以视为其子对象的容器。所以子对象不会在超出父对象的范围显示，且子对象的位置是相对于父对象进行计算的。

例如当父对象的位置是(100, 120)，而子对象设置的位置是(50, 70)时，子对象相对于屏幕的实际位置是(100+50=150, 120+70=190)。而当父对象的位置移动时，子对象的位置也会跟随移动，同样是上面的例子，当父对象移动到(50, 60)的位置之后，子对象的实际位置也会移动到(50+50=100, 60+70=130)。

一个没有父对象的object，即根节点，在LVGL中被称为screen。从名字可以看出，screen是承载布局的基本对象。在使用lv_obj_create()创建object时，需要携带一个parent参数用来指定新建对象的父对象。如果parent为NULL，则LVGL会认为当前正在创建的是一个screen，会自动把这个object的长宽设置为显示器的长宽，并把当前对象加入到screen列表中。

创建完screen之后，需要使用lv_scr_load()函数将创建好的screen加载到默认显示器中。LVGL在进行渲染时，会从当前显示器的screen开始以深度优先的方式遍历整个对象树，逐级渲染每一个object。这样做所达成的效果就是先创建的先渲染，后创建的后渲染，后创建的会盖在先创建的object之上。

#### 4.2 LVGL样式

style，即样式，是LVGL能构建出丰富多变的GUI的灵魂。LVGL在设计样式系统时大量参考了CSS (Cascading Style Sheet，在网页前端开发中使用的样式系统)的设计，所以CSS的主要特性LVGL的样式系统基本都支持，有CSS基础的人上手这套系统非常容易。

LVGL中样式的基本单位是一个lv_style_t结构体，用于存储放有所有样式属性的列表。一个lv_style_t结构体可以绑定给多个object上，类似于CSS中的class概念。

设置样式时有两种方式，一种是创建一个lv_style_t结构体，使用lv_style_set_xxx系列函数设置样式属性，最后使用lv_obj_add_style()函数将创建的lv_style_t绑定给object。当一系列对象拥有共同样式时，使用这种方法可以大量节约内存和时间。

另一种方式是直接使用lv_obj_set_style_xxx系列函数直接对object的样式属性进行设置。在设置时LVGL会自动为目标object创建它专属的lv_style_t结构体，并将样式属性设置进去。在object被删除时，该对象专属的lv_style_t结构体也会一并被释放，不用手动去管理内存，比较省心，适合单个对象少量样式时使用。

除此之外，LVGL的样式系统还支持类似CSS中psuedo-classes和psuedo-elements的state与part机制，继承与级联机制等等。这些“高级特性”将在后面布局使用到的时候进行介绍。

### 5. 改造第一个LVGL界面

在了解了一些基本概念之后，我们来美化一下Hello World界面。

首先是背景，黑色背景过于无趣，我们改成红色：

```c
 lv_obj_set_style_bg_color(screen, lv_color_make(255, 0, 0), LV_PART_MAIN);
```

lv_color_make()是一个LVGL提供的工具函数，用于通过RGB值创建一个颜色。

改完背景色之后，我们再来给label换个字体。在LVGL中，字体也是style的一个属性，所以使用lv_obj_style_set_text_font()函数进行设置：
```c
 lv_obj_set_style_text_font(label, &lv_font_montserrat_48, LV_PART_MAIN);
```

lv_font_montserrat_48是一个LVGL的内置字体，在Example工程中也开启了，所以可以直接使用。

然后我们为label标签设置一个半透明的背景色，和一个圆角效果：

```c
lv_obj_set_style_bg_color(label, lv_color_black(), LV_PART_MAIN); // 设置背景色为黑色
lv_obj_set_style_bg_opa(label, LV_OPA_50, LV_PART_MAIN); // 设置背景透明度为50%
lv_obj_set_style_radius(label, 10, LV_PART_MAIN); // 设置圆角半径为10像素
```

最后，我们在窗口中加入一个按钮，并在按钮中间添加一个label来显示内容。由于Example工程没有使用LVGL的默认主题，所以我们创建出来的按钮并没有默认样式，我们还需要给它加上一些样式：
```c
lv_obj_t *btn = lv_btn_create(screen); // 以screen为父对象创建一个btn控件
lv_obj_set_size(btn, 200, 50); // 将btn控件的size设置为宽200px，高50px
lv_obj_set_pos(btn, 127, 300); // 将btn控件的位置设置为(127, 300)
lv_obj_set_style_bg_color(btn, lv_palette_main(LV_PALETTE_BLUE), LV_PART_MAIN); // 将btn控件的背景色设置为主调色盘中的蓝色
lv_obj_set_style_bg_opa(btn, LV_OPA_COVER, LV_PART_MAIN); // 将btn控件的背景透明度设置为不透明
lv_obj_set_style_radius(btn, LV_RADIUS_CIRCLE, LV_PART_MAIN); // 将btn控件的圆角设置为完全圆形
lv_obj_t *btn_label = lv_label_create(btn); // 以btn控件为父对象创建一个label控件
lv_label_set_text(btn_label, "Click Me"); // 设置label内容为"Click Me"
lv_obj_center(btn_label); // 将label控件居中（btn控件的正中间）
```

现在的btn控件还没有任何的点击效果，点击之后也没有任何的反应。这些内容将留到下一篇文章进行介绍。

最终的layout代码如下：
```c
 void my_first_lvgl_layout(void)
{
	lv_obj_t *screen = lv_obj_create(NULL);
	lv_obj_set_style_bg_color(screen, lv_color_make(255, 0, 0), LV_PART_MAIN);
	lv_obj_set_style_bg_opa(screen, LV_OPA_COVER, LV_PART_MAIN);
	lv_obj_t *label = lv_label_create(screen);
	lv_obj_set_style_text_font(label, &lv_font_montserrat_48, LV_PART_MAIN);
	lv_obj_set_style_bg_color(label, lv_color_black(), LV_PART_MAIN);
	lv_obj_set_style_bg_opa(label, LV_OPA_50, LV_PART_MAIN);
	lv_obj_set_style_radius(label, 10, LV_PART_MAIN);
	lv_label_set_text(label, "Hello World!");
	lv_obj_center(label);
	lv_obj_t *btn = lv_btn_create(screen);
	lv_obj_set_size(btn, 200, 50);
	lv_obj_set_pos(btn, 127, 300);
	lv_obj_set_style_bg_color(btn, lv_palette_main(LV_PALETTE_BLUE), LV_PART_MAIN);
	lv_obj_set_style_bg_opa(btn, LV_OPA_COVER, LV_PART_MAIN);
	lv_obj_set_style_radius(btn, LV_RADIUS_CIRCLE, LV_PART_MAIN);
	lv_obj_t *btn_label = lv_label_create(btn);
	lv_label_set_text(btn_label, "Click Me");
	lv_obj_center(btn_label);
	lv_scr_load(screen);
}
```

编译，下载，来看看效果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/0030910738494d72bff4c5e887fdae88.png)

可以看到，我们设置的样式和新增加的控件都正确显示了。本文通过一个简单的layout例子，介绍了如何在GR5526
SDK中LVGL Example的基础上构建一个简单的LVGL界面。下一篇我将通过为最后添加的btn控件添加按下的动画和事件处理函数，来让这个界面真正可以交互起来。
