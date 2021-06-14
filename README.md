# WeTalk

## 相关常量设置
### `Smart_agent.py`
- `Natural_agent`
  > 智能体类，对智能体相关属性进行定义
    - status (int):
        > 智能体对信息的接收/置信状态
      
| CodeName    | Meaning    |
| :--------:  | :-----: |
| 0        | 易感染      |
| 1        | 已感染      |
| 2        | 已恢复      |
| 2        | 已免疫      |

### `Information.py`
- `Information`
  > 信息类，对信息本身属性进行定义
    - platform (int):
        > 信息流通平台
    
| CodeName    | Meaning    |
| :--------:  | :-----: |
| 0        | 微信      |
| 1        | 微博      |