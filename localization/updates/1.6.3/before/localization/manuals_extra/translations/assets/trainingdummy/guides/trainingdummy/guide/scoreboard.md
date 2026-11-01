---
navigation:
  title: 排行榜假人
  parent: index.md
  position: 2
item_ids:
  - trainingdummy:scoreboard_dummy_spawner
---

# 排行榜假人

第二种假人变体, 记录落在其身上的单次最高伤害, 而不是累计总量, 并将其报告到排行榜.

---

## 入门

<div alignItems="center" fullWidth={true}>
<ItemImage id="trainingdummy:scoreboard_dummy_spawner" scale="2.5" />
</div>

- 用一个训练假人和一颗钻石**合成**一个.

- 像普通假人一样**放置**它.

- **击打它**: 如果伤害足够高, 能进入前 10 名, 就会被加入排行榜.

- 手持木棍**右键点击**以打开排行榜, 查看你的排名.

- 用木棍**击打它**以将其移除, 它会掉落一个可重新放置的训练假人.

---

## 本地与全局

每个服务器都维护自己的**本地**排行榜, 仅收录前 10 名伤害.

还有一个在所有服务器之间共享的**全局**排行榜. 它**默认关闭**: 服务器所有者必须在服务器配置中开启 `globalLeaderboardEnabled`, 在此之前"全局"标签页只会告知你这一点. 启用后, 只会发送你的昵称和破纪录伤害的数值. 全局排行榜每周重置; 本地排行榜从不重置.

当前显示排行榜上的第 1 名玩家会在其名字旁渲染皮肤; 点击并拖动它即可旋转.

---

## 武器黑名单

服务器所有者可以阻止特定武器 (或整个模组) 上榜. 如果使用这类东西造成的伤害没有出现在排行榜上, 原因就在于此.

以下内容在所有服务器上都始终被阻止:

- Morgan Sword (Mahou Tsukai)
- Forbidden Butcher Knife (Occultism Extra Spirits)
- 来自 Avaritia 的任何物品
- 来自 Modern Industrialization 的任何物品
- 名称中包含 "Infinity" 的任何物品
- 名称中包含 "Quantum" 的任何物品

服务器所有者还可以在此列表之上额外阻止更多武器.
