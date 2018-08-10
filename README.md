# 一键下载: 将知乎专栏导出成电子书


[![GitHub issues](https://img.shields.io/github/issues/ronething/ZhiHuZhuanLanToPDF.svg)](https://github.com/ronething/ZhiHuZhuanLanToPDF/issues)
[![GitHub forks](https://img.shields.io/github/forks/ronething/ZhiHuZhuanLanToPDF.svg)](https://github.com/ronething/ZhiHuZhuanLanToPDF/network)
[![GitHub stars](https://img.shields.io/github/stars/ronething/ZhiHuZhuanLanToPDF.svg)](https://github.com/ronething/ZhiHuZhuanLanToPDF/stargazers)


参考自 ： https://gitee.com/crossin/snippet/tree/master/get_zhihu

---

## 准备工作

需要安装库：requests、bs4、pdfkit(可要可不要 程序代码会使用pdfkit，pdfkit会调用wkhtmltopdf，而wkhtmltopdf会调用windows中的wkhtmltopdf.exe来转化html为pdf。所以可以直接用`os.system(cmd)`操作)

手动安装 **wkhtmltopdf**  https://wkhtmltopdf.org/

安装可参考 https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf

关于no such file or directory:b'' 这种错误在python中出现时，意味着有.exe文件需要被调用，而该.exe文件没有被安装或者在控制面板的环境变量中没有添加该.exe的路径。另外，有时候需要改pdfkit代码为下列两句，才可消除错误：

```
config=pdfkit.configuration(wkhtmltopdf=r"D:\software\wkhtmltopdf\bin\wkhtmltopdf.exe")
```

---

## 实现效果

- 输入专栏名字 获取每篇文章链接

  ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fu53ebs60uj20it0bet9p.jpg)

- 获取文章详情 保存为`html`文件

  ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fu53fdtfi1j20gq06v0sr.jpg)

  ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fu53g48wu0j20jt08s0u1.jpg)

- 生成`pdf`

  ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fu53d52zjpj20hu0eeq34.jpg)

---

## TODO

* [ ] 速度太慢了，要搞快点。

