---
title: 能量
entryId: stellaris:machines
iconType: item
associatedBlocks: [stellaris:cable_t1]
---

群星 中的每台机器都依靠同一种东西运行: 能量, 以 FE 计量.本页说明能量如何在你的基地中流动.各台机器都有自己的页面.

本百科中的每个数值都基于默认能量倍率(x15).服务器可在 群星 配置中调高或调低它, 届时所有发电机, 机器, 缓存和线缆都会按相同比例缩放.

[image=stellaris:textures/wiki/rendered_blocks/power_bank width=96 height=96]



**一切都有缓存**

机器与发电机的连接方式, 并不像台灯插在插座上那样.每台机器, 每台发电机和每个 [ref=stellaris:machines/power_bank]储能电池[ref] 都拥有自己私有的能量池, 而 [ref=stellaris:machines/cables]线缆[ref] 所做的只是把能量从较满的缓存移到较空的缓存.

由此产生一个值得记住的结果: 切断供电后机器还会运行一段时间, 因为它在花掉自己已经储存的能量.一台 [ref=stellaris:machines/oxygen]氧气分配器[ref] 若处于充满的 192 000 FE 缓存上, 即使发电机早已停转, 也能让房间保持可呼吸很久.



**产生能量**

四台发电机, 大致按获取难度排序:
- [ref=stellaris:machines/solar_panel]太阳能板[ref]: 15 FE/t, 且只有阳光照到它时.
- [ref=stellaris:machines/star_light_panel]星光板[ref]: 15 FE/t, 适合在太空中工作的版本.
- [ref=stellaris:machines/coal_generator]燃煤发电机[ref]: 45 FE/t, 燃烧煤炭.
- [ref=stellaris:machines/diesel_generator]柴油发电机[ref]: 75 FE/t, 燃烧 [ref=stellaris:items/diesel]柴油[ref], 每 mB 375 FE.

单台 75 FE/t 的柴油发电机就足以运行一台电解器或燃料精炼厂, 或者一个分配器, 一个扩散器和几盏灯.基地靠增加发电机来扩张, 而不是靠找到一台更大的发电机.



**传输能量**

线缆传输 300 FE/t, 仅此而已, 它不会输送流体, 流体交给 [ref=stellaris:machines/pipes]管道[ref].因此一段线缆最多能承接四台柴油发电机的输出, 之后线缆本身就会成为瓶颈.



**储存能量**

储能电池就是一个没有接任何东西的缓存: 它吸收多余的能量, 并在发电机跟不上时返还.1 级可储存 240 000 FE.

它也是给装备充电的地方.把航天服头盔放入其输出槽, 即可为夜视模块和石油探测模块所用的电池充能.太阳能板和星光板也能直接为物品充电, 速率为 150 FE/t, 比它们自身的发电速度更快.



*趣闻*: 储能电池被破坏时会保留电量, 因此你可以带着一块满电的电池前往还没有发电机的站点.

[item=stellaris:cable_t1 onlyIcon]
