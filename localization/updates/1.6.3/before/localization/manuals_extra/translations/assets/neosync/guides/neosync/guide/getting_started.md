---
navigation:
  title: 入门
  icon: minecraft:golden_apple
  parent: index.md
  position: 1
---

# <Color id="light_purple">入门</Color>

本页从零开始介绍第一个躯壳, 直到你完成首次同步.

***
## <Color id="gold">第 1 步: 同步核心</Color>

合成一个<ItemLink id="sync_core"/>.它是每个 NeoSync 方块的关键成分.

<RecipeFor id="sync_core"/>

***
## <Color id="gold">第 2 步: 壳体培育仓</Color>

合成一个<ItemLink id="shell_constructor"/>并放置它.它有两格高, 因此要在其上方留出空间.

<RecipeFor id="shell_constructor"/>

空手右击培育仓以提供基因样本.

<Color id="red">警告</Color>: 默认配置下, 采样会消耗 20 点生命值 (极限模式为 40 点), 也就是你整条生命栏.请先吃一个金苹果或附魔金苹果, 手持不死图腾, 或请服务器管理员在配置中开启 `warnPlayerInsteadOfKilling`.如果你死亡, 躯壳仍会开始培育.

***
## <Color id="gold">第 3 步: 为培育仓供能</Color>

合成一台<ItemLink id="treadmill"/>并放置, 使它的任意一半接触培育仓.它的放置方式与床相同: 两格长, 从你身边向外延伸, 较远的一格为前端.

<RecipeFor id="treadmill"/>

把猪或狼引到前端方块上.动物会原地奔跑, 培育仓随之充能.培育仓上的比较器会报告培育进度, Jade 会以百分比显示.

任何指向培育仓的 Forge 能量线缆或发电机同样有效.默认情况下, 培育一个完整躯壳需要 256000 FE.

***
## <Color id="gold">第 4 步: 壳体存放仓</Color>

合成一个<ItemLink id="shell_storage"/>并把它放在你希望能前往的地点.

<RecipeFor id="shell_storage"/>

给它红石信号或输入 FE.有能量时门会打开.

***
## <Color id="gold">第 5 步: 同步</Color>

走进打开门的存放仓.壳体选择仓会打开, 按世界分组显示你拥有的每一个已完成的躯壳.点击一个躯壳, 你的意识就会进入其中.你原来的躯体连同携带的所有物品留在存放仓中.

关于死亡后会发生什么, 跨维度旅行如何运作以及如何重命名躯壳, 参见[同步](syncing.md).
