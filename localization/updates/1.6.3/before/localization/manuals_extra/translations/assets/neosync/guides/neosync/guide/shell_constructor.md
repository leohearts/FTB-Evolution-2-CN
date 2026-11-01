---
navigation:
  title: 壳体培育仓
  icon: neosync:shell_constructor
  parent: index.md
  position: 3
item_ids:
  - neosync:shell_constructor
  - neosync:zero_point_shell_constructor
---

# <Color id="light_purple">壳体培育仓</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="shell_constructor" scale="2"/>
  用你自己的样本培育一具新躯体.
</Column>

***
## <Color id="gold">配方</Color>

<RecipeFor id="shell_constructor"/>

培育仓有两格高.放置时请在其上方留出一格空位.

***
## <Color id="gold">采集样本</Color>

空手右击培育仓.它会采集一份基因样本, 并开始培育属于你的躯壳.

<Color id="red">采样会消耗 20 点生命值, 极限模式下为 40 点.</Color>这相当于一整条生命栏, 因此毫无准备时会杀死你.规避方法:

* 先吃一个金苹果或附魔金苹果以获得伤害吸收.
* 在任意一只手中手持不死图腾.
* 让服务器开启 `warnPlayerInsteadOfKilling`, 它会在你生命值不足时拒绝采样, 而不是杀死你.

如果你确实死亡, 躯壳仍会开始培育.一个培育仓同一时间只能培育一个躯壳, 它会一直留在那里, 直到你同步进去.

***
## <Color id="gold">供能</Color>

默认情况下, 一个躯壳需要 256000 FE (`shellConstructorCapacity`), `shellConstructionSpeed` 决定充能速度.任何 Forge 能量源都可以: 贴着培育仓的<ItemLink id="treadmill"/>, FE 线缆, 或其他模组的发电机.

贴着培育仓的比较器会输出培育进度.Jade 会显示所有者和百分比.

在创造模式下开启 `enableInstantShellConstruction` 后, 躯壳会瞬间完成.

***
## <Color id="gold">颜色</Color>

手持染料潜行右击培育仓, 可为其饰边重新着色.在其中培育的躯壳会在壳体选择仓中采用该颜色, 便于区分不同躯体.

***
## <Color id="gold">零点壳体培育仓</Color>

<Row>
  <ItemImage id="zero_point_shell_constructor"/>
  ### <Color id="aqua">零点壳体培育仓</Color>
</Row>

用下界之星升级培育仓.它无需供能, 并可瞬间完成躯壳.采样仍会消耗生命值.

<RecipeFor id="zero_point_shell_constructor"/>
