---
navigation:
  title: 同步
  icon: minecraft:ender_eye
  parent: index.md
  position: 6
---

# <Color id="light_purple">同步</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="minecraft:ender_eye" scale="2"/>
  在躯体之间转移你的意识.
</Column>

***
## <Color id="gold">壳体选择仓</Color>

走进打开门的<ItemLink id="shell_storage"/>, 壳体选择仓就会打开.它是一个环形菜单, 你拥有的每个躯壳对应一个条目.

* 躯壳按世界分组.使用上下箭头切换世界, 使用左右箭头在拥挤的世界中翻页.
* 每个条目显示躯壳的坐标, 对于仍在培育中的躯壳还会显示进度.
* 右击躯壳可重命名.回车保存, Esc 取消.
* 位于<ItemLink id="manual_shell_storage"/>中的躯壳会标记为手动.

点击躯壳即可同步.你当前的躯体连同携带的一切留在原地, 而你会在所选躯壳中醒来.每个躯壳都保留自己的物品栏, 经验等级和游戏模式.

同步可跨维度进行, 包括自定义维度.第一次这样做时, 你会获得灵魂出窍进度.

***
## <Color id="gold">在躯壳中死亡</Color>

在躯壳中死亡不会计入你的死亡次数.接下来会发生什么取决于你所在的位置:

* <Color id="aqua">在躯壳中, 且有另一个已完成的躯壳可用</Color>: 你会直接同步到下一具躯体.死亡的躯壳会在死亡地点掉落物品栏, 因此坟墓类模组会将其收集.
* <Color id="aqua">在躯壳中, 但无处可去</Color>: 普通死亡.你会照常重生.
* <Color id="aqua">在你原本的躯体中</Color>: 普通死亡.当你的第一具躯体死亡时, 永远不会为你自动选择躯壳.

位于<ItemLink id="manual_shell_storage"/>中的躯壳永远不会被自动选中.

服务器可以通过 `autoSyncOnDeath` 完全关闭自动同步.此时你会看到普通死亡界面并照常重生, 所有躯壳仍可走进去使用.

***
## <Color id="gold">选择哪个躯壳</Color>

当有多个躯壳符合条件时, `syncPriority` 配置决定顺序.其默认值 `NATURAL` 优先选择你原本的躯体.`NEAREST` 优先选择最近的躯壳, 任意染料颜色名则优先选择存放在该颜色存放仓中的躯壳.可以列出多个值, 第一个匹配到躯壳的值生效.

***
## <Color id="gold">幽灵躯壳</Color>

如果在存放仓中仍有躯壳时存放仓被破坏或区块被回滚, 该躯壳可能会残留在壳体选择仓中, 但背后没有躯体.管理员可以使用 `/neosync ghostshells` 清理它们.参见[命令](commands.md).
