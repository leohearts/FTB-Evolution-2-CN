---
navigation:
  title: 训练假人
  position: 0
item_ids:
  - trainingdummy:dummy_spawner
---

# 训练假人

一个可配置的战斗假人, 用于测试伤害, 装备和模组. 放下它, 击打它, 然后读取数字.

---

## 入门

<div alignItems="center" fullWidth={true}>
<ItemImage id="trainingdummy:dummy_spawner" scale="2.5" />
<GameScene zoom="4">
  <Entity id="trainingdummy:dummy" />
</GameScene>
</div>

- 将训练假人**放置**在地面上, 以召唤一个假人.

- 用任何东西**击打它**, 即可看到伤害数字, 显示在聊天栏或屏幕上 (可配置).

- 手持木棍**右键点击**以打开其物品栏 (盔甲, 饰品, 生命, 显示设置).

- 用木棍**击打它**以将其移除, 它会掉落一个可重新放置的训练假人.

- 在铁砧中用命名牌**重命名它**, 即可赋予它真实 Minecraft 玩家的皮肤.

- 将单个已装载的训练假人**单独放入**任意合成格, 会重置其生命/名称/显示设置, 但保留它记住的装备.

---

## 伤害显示

每个假人都能将其受到的伤害显示为**总计**, **DPS**或**单次**, 按每个假人单独设置, 而非全局设置.

当伤害不是普通物理伤害时, "单次"还会标注伤害类型 (火焰, 冰冻, 爆炸, 闪电, 魔法).

---

## 诱饵

将诱饵放在假人的主手中, 使附近的敌对生物转而以它为目标, 而不是你.

<Column alignItems="center" fullWidth={true}>
<ItemImage id="trainingdummy:lure_bait" scale="2.5" />
</Column>

---

## 排行榜假人

一种变体, 会记录落在其身上的单次最高伤害, 并将其排在**本地**前 10 名排行榜上 (如果服务器启用, 还会排入每周的**全局**排行榜). 用一个训练假人和一颗钻石合成.

完整细节见[排行榜假人](scoreboard.md)页面.

---

## 彩蛋

模组中有一些隐藏惊喜: 某些假人昵称, 甚至一个物品把戏, 都会产生特殊效果. 我们不会在这里剧透, 但你可以在[彩蛋](easter-eggs.md)页面找到列表.
