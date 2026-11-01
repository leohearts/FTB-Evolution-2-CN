---
navigation:
  title: 脉冲激光
  icon: nautec:impulse_laser_module
  position: 13
  parent: submarine/submarine-index.md
item_ids:
  - nautec:impulse_laser_module
---

# <Color id="light_purple">脉冲激光</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="impulse_laser_module" scale="2"/>
  艇首前方的双生光束.
</Column>

脉冲激光模块会向艇首正前方发射两道光束, 如同两把亚特兰蒂斯步枪, 只要你按住发射键就会持续射击.

***

## <Color id="gold">使用</Color>

| | 默认 |
|---|---|
| 蓄能 | 光束出现前需半秒 |
| 提升 | 持续射击 5 秒达到满强度 |
| 能量 | 每刻 400, 升至每刻 1,400 |
| 范围 | 64 格 |
| 每道光束伤害 | 2 升至 6, 外加目标最大生命值的 0.4% 升至 1.25%, 每秒四次 |

在能力栏中选中该模块, 按住攻击键或能力键. 激光蓄能半秒后, 两道光束同时发射. 持续射击越久, 光束越宽越亮, 伤害也越高, 五秒后达到满强度. 松手后光束立刻停止; 再次发射会从蓄能重新开始.

通过调整艇体朝向瞄准: 光束跟随艇首, 而不是你的视线, 即使在自由观察时也是如此. 每道光束会在路径上的第一个生物或固体方块处停止, 同时被两道光束命中的目标会受到两次伤害. 伤害无视护甲, 且光束不会伤及艇体自己的乘员.

***

## <Color id="gold">能量</Color>

达到满强度的激光每秒消耗 28,000 能量, 因此短促点射比一直按住要省得多. 当电池电量过低无法供给, 驾驶员离开艇体, 或模块被取下时, 激光会停止.

所有数值都可配置.

***

### <Color id="aqua">脉冲激光模块配方</Color>

<Recipe id="nautec:impulse_laser_module"/>
