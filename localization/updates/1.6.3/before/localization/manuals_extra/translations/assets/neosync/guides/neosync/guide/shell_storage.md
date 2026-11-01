---
navigation:
  title: 壳体存放仓
  icon: neosync:shell_storage
  parent: index.md
  position: 4
item_ids:
  - neosync:shell_storage
  - neosync:manual_shell_storage
  - neosync:zero_point_shell_storage
---

# <Color id="light_purple">壳体存放仓</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="shell_storage" scale="2"/>
  当你的意识在别处时, 妥善保护躯体.
</Column>

***
## <Color id="gold">配方</Color>

<RecipeFor id="shell_storage"/>

与培育仓一样, 存放仓有两格高.

***
## <Color id="gold">供能与门</Color>

存放仓需要能量来维持躯壳存活.它接受红石信号 (除非关闭 `shellStorageAcceptsRedstone`) 或 Forge 能量.其缓冲可存储 320 FE, 默认每刻消耗 16 FE.

有能量时门会打开.走进打开门的存放仓可调出壳体选择仓, 或走进空的存放仓将当前躯体留在那里.

失去能量的存放仓会让其中的躯壳继续存活 `shellStorageMaxUnpoweredLifespan` 刻 (默认 20 刻), 之后其中的躯壳死亡.

***
## <Color id="gold">实用技巧</Color>

* 手持染料潜行右击, 可为饰边和其中的躯壳着色.颜色会显示在壳体选择仓中, 并可影响 `syncPriority`.
* 指向存放仓的漏斗可以为存放的躯壳装备或卸下盔甲和工具.
* 比较器可读取培育进度或物品栏占用情况.手持扳手物品 (默认为木棍, 由配置中的 `wrench` 设置) 右击存放仓, 可在两者之间切换.
* 用任意镐挖掘存放仓或培育仓即可掉落方块.无需精准采集.

***
## <Color id="gold">手动壳体存放仓</Color>

<Row>
  <ItemImage id="manual_shell_storage"/>
  ### <Color id="aqua">手动壳体存放仓</Color>
</Row>

一种存放仓, 其中的躯壳在你死亡时永远不会被自动选中.适合为单一任务打造的躯体, 例如装满工具的采矿躯体, 或停放在远处前哨的躯体.像其他存放仓一样走进去, 即可手动同步到其中.

<RecipeFor id="manual_shell_storage"/>

***
## <Color id="gold">零点壳体存放仓</Color>

<Row>
  <ItemImage id="zero_point_shell_storage"/>
  ### <Color id="aqua">零点壳体存放仓</Color>
</Row>

用下界之星升级存放仓.它无需红石或 FE, 靠近时门会自动打开, 其中的躯壳永不腐坏.

<RecipeFor id="zero_point_shell_storage"/>
