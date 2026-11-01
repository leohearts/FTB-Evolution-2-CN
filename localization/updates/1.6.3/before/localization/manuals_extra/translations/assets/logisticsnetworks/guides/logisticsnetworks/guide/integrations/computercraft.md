---
navigation:
  title: ComputerCraft 集成
  parent: integrations/index.md
  position: 1
---

# ComputerCraft 集成

安装 [CC: Tweaked](https://modrinth.com/mod/cc-tweaked) 后, 电脑还可作为外设使用. 脚本可以读取电脑屏幕显示的一切内容 (网络, 频道, 节点, 节点图和实时 I/O 遥测数据), 并将其绘制到显示器上.

## 连接

将一台 CC 电脑放在电脑旁边, 或用有线调制解调器连接两者. 外设类型为 `logistics_computer`:

```lua
local lc = peripheral.find("logistics_computer")
```

## 所有权

电脑归放置它的玩家所有. 脚本只能看到该玩家可以打开的网络, 遵循服务器的节点访问规则和 FTB Teams. 任何将 CC 电脑连接到它的人都能读取这些网络, 因此请把它放在只有你能接触到的地方.

在此更新之前放置的电脑没有所有者. 将其破坏并重新放置, 即可在 ComputerCraft 中使用它.

## 方法

`net` 是网络 ID 或其准确名称. 频道列表按屏幕顺序排列, 每个条目的 `index` 就是 [I/O 监视器](../computer/io-monitor.md)中显示的 `CH` 编号, 从 0 开始, 因此 CH0 对应 `channels[1]`. 图的边 `channels` 也保存 CH 编号.

| 方法 | 返回 |
|---|---|
| `listNetworks()` | `{ {id, name, nodeCount, starred, color, createdAt}, ... }` |
| `getChannels(net)` | `{ {index, name, type, nodeCount}, ... }`: 当频道没有已启用的节点时, `type` 为 nil |
| `getNodes(net)` | `{ {id, label, block, pos, attachedPos, dimension, visible, highlighted}, ... }`: 仅包含已加载的节点 |
| `getGraph(net)` | `{ name, totalNodes, vertices, edges }`: 顶点包含 `key, label, x, y, nodes`; 边包含 `from, to, type, channels` |
| `watch(net)` | 为此电脑启动实时遥测 |
| `unwatch(net)` | 停止遥测 |
| `getFlow(net)` | 最后一次遥测采样, 在第一秒之前为 nil; 如果网络未被监视则报错 |

类型为 `item`, `fluid` 和 `energy`.

## 实时遥测

调用 `watch` 后, 每秒会到达一个 `logistics_flow` 事件:

```lua
local _, side, networkId, sample = os.pullEvent("logistics_flow")
-- sample.channels[1].total, sample.channels[1].resources[1].displayName
```

每个频道都有 `index`, `type`, `total` (那一秒内移动的数量, 使用 I/O 监视器的单位) 和 `resources`: 前 16 种物品或流体, 包含 `kind`, `name`, `displayName` 和 `amount`. 能量频道的资源列表为空.

电脑重启或断开连接时, 监视会结束, 因此请在你的 `startup` 脚本中调用 `watch`. 如果所有者失去对网络的访问权限或网络被删除, 监视也会停止, 且不会报错.

## 示例

在连接的显示器上显示每个频道的实时速率:

```lua
local lc = peripheral.find("logistics_computer")
local mon = peripheral.find("monitor")
local net = "Main Base"

mon.setTextScale(0.5)
lc.watch(net)
while true do
  local _, _, _, sample = os.pullEvent("logistics_flow")
  mon.clear()
  for i, ch in ipairs(sample.channels) do
    mon.setCursorPos(1, i)
    mon.write(("CH%d %-8s %d/s"):format(ch.index, ch.type or "-", ch.total))
  end
end
```
