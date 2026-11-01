---
navigation:
  title: 模组联动
  icon: minecraft:comparator
  parent: index.md
  position: 9
---

# <Color id="light_purple">模组联动</Color>

以下内容均为可选.NeoSync 在没有它们时也能以相同方式运行.

***
## <Color id="gold">JEI</Color>

每个 NeoSync 方块都有信息页, 跑步机能源类别会列出跑步机接受的每种实体及其当前每刻 FE.

***
## <Color id="gold">Jade</Color>

查看培育仓, 存放仓或跑步机, 可显示所有者, 培育进度, 饰边颜色, 供能状态和能量水平.

***
## <Color id="gold">Curios</Color>

Curios 饰品栏属于躯体.每个躯壳保留自己的饰品, 当你同步离开时, 它们会随躯体留下.

***
## <Color id="gold">Mekanism</Color>

辐射也属于躯体.躯壳会保留你在其中时吸收的剂量, 新培育的躯壳从零开始, 同步不会把辐射带在身上.

***
## <Color id="gold">Sable and Create Aeronautics</Color>

壳体存放仓, 培育仓和跑步机都能在移动或旋转的飞艇上工作.走进甲板上的存放仓会打开壳体选择仓, 同步到停在另一艘飞艇上的躯壳也能正常工作, 跑步机上的动物会相对飞船原地奔跑.每个躯壳都会记住自己所在的飞艇.

***
## <Color id="gold">坟墓模组</Color>

在原本的躯体中死亡属于普通死亡, 因此坟墓类模组会照常运作.

在有其他可用躯壳时于躯壳中死亡则不同: 死亡和掉落事件会触发, 因此会在死亡躯壳处放置坟墓并包含其完整物品栏, 但没有重生过程, 所以重生事件永远不会触发.对 Simple Tombs 而言, 这意味着灵魂绑定的 `KEEPPARTS` 选项不会在自动同步中延续.如果你希望行为一致, 请设置 `KEEPPARTS=NONE`, 并依赖坟墓.
