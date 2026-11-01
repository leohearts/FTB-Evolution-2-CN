---
navigation:
  title: 自定义细菌
  icon: minecraft:command_block
  position: 14
  parent: aquatic_biology/aquatic_biology-index.md
---

# <Color id="light_purple">自定义细菌</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="minecraft:command_block" scale="2"/>
  管理员命令可为任何物品创建新的细菌菌株.
</Column>

本页面向服务器管理员和整合包作者. 这些命令需要管理员权限(等级 2).

***

## <Color id="gold">创建菌株</Color>

`/nautec bacteria generate <name> <item> [rarity]`

创建一个名为 `<name>`, 产出 `<item>` 的菌株, 并同时创建一个以该物品本身为营养物的培养配方, 一个使用相同营养物的菌落喂养配方, 以及一个以该物品为催化剂的突变配方. 稀有度决定起始属性, 培养生长量, 突变几率和[菌株产量](production_rates.md), 并决定它从哪个菌株突变而来:

| 稀有度 | 突变自 | 菌株产量 |
|---|---|---|
| common | 嗜岩石菌 | 1 |
| uncommon(默认) | 嗜金属菌 | 0.8 |
| rare | 嗜铁菌 | 0.6 |
| epic | 嗜金菌 | 0.4 |
| legendary | 嗜金刚菌 | 0.12 |

`/nautec bacteria generate-tag <name> <item> <tag> [rarity]` 功能相同, 但使用整个物品标签作为营养物.

在任一命令末尾加上 `preview`, 可在聊天栏中打印文件, 点击即可复制, 而不会写入任何内容.

***

## <Color id="gold">移植来源</Color>

`/nautec bacteria obtain <name> <block> <biometag> <chance>`

让玩家可以从 `<block>` 移植该菌株, 适用于 `<biometag>` 中的任意生物群系, 几率为 0 到 1. 请选择一个 海蓝科技 尚未从中移植的方块.

***

## <Color id="gold">管理它们</Color>

* `/nautec bacteria list-generated` 列出每个生成的菌株, 它产出什么, 以及它拥有哪些配方.
* `/nautec bacteria delete-generated <name>` 删除某个菌株的文件及其移植条目.

所有内容都存放在 `config/nautec/generated_pack` 中, 该实例中的每个世界共享此目录. 运行 `/reload` 以加载新的配方和移植来源. 新菌株本身会在你下次加入世界时加载.
