# GraphLab Matching API

FastAPI 后端服务，提供图匹配算法接口：Hopcroft-Karp、Blossom。支持步骤记录与可视化。

## 接口文档

### POST `/api/graph/{graph_id}/match`

#### 请求体

```json
{
  "algorithm": "hopcroft-karp"
}
```

#### 响应体

```json
{
  "steps": [ ... ],
  "summary": {
    "algorithm": "hopcroft-karp",
    "total_matched": 4,
    "time_taken": "模拟耗时"
  }
}
```

## 启动方法

```bash
uvicorn main:app --reload
```

确保本地已有 `graph_store.py` 中注册的图。