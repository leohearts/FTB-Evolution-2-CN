---
navigation:
  title: 命令
  icon: minecraft:command_block
  parent: index.md
  position: 7
---

# <Color id="light_purple">命令</Color>

所有内容都位于 `/neosync` 下, 需要权限等级 2.`anchor` 和 `ghostshells` 在单人游戏中也可由主机使用.

***
## <Color id="gold">/neosync select [targets]</Color>

在目标所在位置为他们打开壳体选择仓, 无需存放仓.没有已完成躯壳的玩家会被跳过并收到一条消息.

站在空的存放仓中时, 它的作用与普通同步相同: 躯体留在存放仓中.不在存放仓附近时, 躯体无处安放, 因此玩家会被杀死, 并在重生时进入所选躯壳.已经处于死亡界面的玩家也可以选择躯壳, 并会直接在躯壳中抵达, 而不是在出生点.

***
## <Color id="gold">/neosync anchor</Color>

重生锚点是一个重生点, 它会像躯壳一样出现在壳体选择仓中, 但背后没有方块.同步到它会在这组坐标处创建一具满生命值, 空物品栏的全新躯体.

* `anchor set <targets> <dimension> <x y z> [temporary]` 为每个目标设置一个重生锚点.传入 `true` 可获得一次性重生锚点, 使用后立即消失.
* `anchor ensure <targets> <dimension> <x y z>` 只为没有可同步目标的玩家设置一次性重生锚点.可以安全地在计时器或登录钩子中运行.
* `anchor list <targets>` 列出重生锚点, 并标记出一次性的锚点.
* `anchor remove <targets> [dimension x y z]` 移除一个重生锚点; 不提供坐标时移除全部.

***
## <Color id="gold">/neosync ghostshells</Color>

`ghostshells <sync|remove|repair> <targets> [x y z]` 用于处理在壳体选择仓中显示, 但已不存在于世界中的躯壳.重生锚点永远不会被改动.

* `sync` 修复能修复的躯壳, 并删除其余的.
* `repair` 修复能修复的躯壳, 并报告其余的, 但不删除.
* `remove` 直接删除幽灵躯壳, 不尝试修复.

不提供坐标时, 清理范围覆盖该玩家拥有的所有躯壳, 并将每个躯壳标记为已完全培育.

***
## <Color id="gold">/neosync purge</Color>

`purge <players> [dimension]` 删除玩家的躯壳, 包括玩家条目和方块中的副本.其中存放的躯体会在方块处掉落物品栏和经验.省略维度将清除所有躯壳.
