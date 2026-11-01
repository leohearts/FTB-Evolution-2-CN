---
navigation:
  title: 隐形模块
  icon: nautec:stealth_module
  position: 10
  parent: submarine/submarine-index.md
item_ids:
  - nautec:stealth_module
---

# <Color id="light_purple">隐形模块</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="stealth_module" scale="2"/>
  两分钟不被发现.
</Column>

发射隐形模块可让艇体及其乘员在两分钟内不被生物发现, 代价是降低一些速度.

***

## <Color id="gold">使用</Color>

| | 默认 |
|---|---|
| 每次使用能量 | 50,000 |
| 持续 | 2 分钟 |
| 生效期间速度 | 推力减少 15% |
| 冷却 | 发射后 130 秒 |

发射的瞬间, 32 格内所有正在追猎艇体或艇上人员的生物都会放弃. 接下来两分钟内, 无论靠得多近, 任何生物都无法将艇体或其乘员选为目标. 隐形生效期间, 其槽位会显示亮色细条.

隐形期间艇体损失 15% 的推力. 如果需要快速脱离, 可同时发射[推进模块](booster_module.md).

隐形结束后, 模块还需 10 秒才能再次发射, 生物也会像平常一样注意到你.

所有数值都可配置.

***

### <Color id="aqua">隐形模块配方</Color>

<Recipe id="nautec:stealth_module"/>
