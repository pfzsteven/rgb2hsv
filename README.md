# rgb2hsv

## 使用说明

### 输出格式 

```python
hex:h,s,v
```

### Example1: 单个rgb hex字符串

- 命令行输入:

```shell
> python3 hsv.py f2d4b1
```

- 打印结果:

```shell
f2d4b1:32.31,0.27,0.95
```

### Example2: 多个rgb hex字符串以空格隔开

- 命令行输入:

```shell
> python3 hsv.py f2d4b1	f3cfb4 f5d8d1
```
- 打印结果:
 
```shell
f2d4b1:32.31,0.27,0.95
f3cfb4:25.71,0.26,0.95
f5d8d1:11.67,0.15,0.96
```

### Example3: 多个rgb hex字符串连在一起

- 命令行输入:

```shell
> python3 hsv.py f2d4b1f3cfb4f5d8d1
```

- 打印结果:

```shell
f2d4b1:32.31,0.27,0.95
f3cfb4:25.71,0.26,0.95
f5d8d1:11.67,0.15,0.96
```
