---
navigation:
  title: 跑步机
  icon: neosync:treadmill
  parent: index.md
  position: 5
item_ids:
  - neosync:treadmill
---

# <Color id="light_purple">跑步机</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="treadmill" scale="2"/>
  畜力驱动的工业.
</Column>

***
## <Color id="gold">配方</Color>

<RecipeFor id="treadmill"/>

***
## <Color id="gold">放置</Color>

跑步机有两格长, 放置方式与床相同: 它从你身边向外延伸, 较远的一格为前端.将任意一半贴着<ItemLink id="shell_constructor"/>或<ItemLink id="shell_storage"/>, 或贴着任何接受 Forge 能量的方块.

***
## <Color id="gold">奔跑者</Color>

把动物引到前端方块上.它会锁定跑步机, 原地奔跑, 并每刻产生能量.能量会输入到接触跑步机任意一半的每个 FE 接收方.

动物在以下情况下不再计为奔跑者: 处于幼年, 被拴绳牵引, 被命令坐下, 受到伤害, 或站在水中.玩家也可以奔跑, 但潜行的玩家不算.

***
## <Color id="gold">每种实体的能量</Color>

来自 `energyMap` 的默认值.服务器管理员可以将任意实体添加到列表中.

| 实体 | FE/tick |
| --- | --- |
| 鸡 | 2 |
| 猪 | 16 |
| 玩家 | 20 |
| 狼 | 22 |
| 村民 | 25 |
| 苦力怕 | 80 |
| 末影人 | 160 |

安装 JEI 后, 跑步机能源类别会列出当前服务器的实时数值.
