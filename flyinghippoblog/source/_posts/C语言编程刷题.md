---
cctitle: C语言编程刷题
date: 2020-12-3
tags:
mathjax: true
---



注释前言

···

<!-- more -->



# Openjudge 计算概率A

## 基础编程练习1

### 1:大象喝水

```c++
#include<iostream>
using namespace std;
int main()
{
	int h = 0, r = 0;
	cin >> h >> r;
	float pi = 3.14159;
	float each = pi * r * r * h;
	int sum = 20 * 1000;
	int out = 0;
	cout << int(sum / each) + 1;
	return 0;
}
```



### 2:苹果和虫子



```c++
#include<iostream>
using namespace std;
int main()
{
	int n = 0, x = 0, y = 0;
	cin >> n >> x >> y;
	if (y%x == 0){cout << n - y / x; }
	else{ cout << n - y / x - 1; }
	system("pause");
	return 0;
}
```



### 3:晶晶赴约会

```c++
#include<iostream>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	if (n == 1 || n == 3 || n == 5)
		cout << "NO";
	else
		cout << "YES";
	system("pause");
	return 0;
}
```



### 4:求一元二次方程的根

太难了  ac不了 补一个别人的代码

```c++
#include<cstdio>
#include<cmath>

int main()
{
	int n;double a,b,c;
	scanf("%d",&n);
	while(n--)
	{
		scanf("%lf%lf%lf",&a,&b,&c);
		double delta=b*b-4*a*c;//判别式
		double ret1=-b/(2*a)+0.0;
		if(delta==0)
			printf("x1=x2=%.5lf\n",ret1);
		else if(delta>0)
		{
			double ret2=sqrt(delta)/(2*a);
			printf("x1=%.5lf;x2=%.5lf\n",ret1+ret2,ret1-ret2);
		}
		else
		{
			double ret2=sqrt(-delta)/(2*a);
			printf("x1=%.5lf+%.5lfi;x2=%.5lf-%.5lfi\n",ret1,ret2,ret1,ret2);
		}
	}
	return 0;
}
```



### 5:鸡兔同笼

```c++
#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	int a = 0;
	cin >> a;
	int min_num = 0, max_num = 0;
	if (a % 2 != 0 || a>=32768)
		cout << "0 0";
	else if (a % 4 == 0)
	{
		min_num = a / 4; max_num = a / 2;
		cout << min_num << " " << max_num;
	}
	else
	{
		min_num = a / 4 + 1;
		max_num = a / 2;
		cout << min_num << " " << max_num;
	}	

	//system("pause");
	return 0;
}

```



### 6:判断闰年

```c++
#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	int a = 0;
	cin >> a;
	if (a % 4 == 0)
	{
		if ((a % 100 == 0 && a % 400 != 0) || (a % 3200 == 0))
			cout << "N";
		else
			cout << "Y";
	}
	else
		cout << "N";

	//system("pause");
	return 0;
}

```



### 7:奇数求和

```c++
#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	int m = 0,n = 0;
	cin >> m>>n;
	int sum = 0;
	for (int i = m; i < n + 1; i++)
	{
		if (i % 2 != 0)
			sum += i;
	}
	cout << sum;

	system("pause");
	return 0;
}

```



### 8:与7无关的数

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int n = 0, sum = 0;
	cin >> n;
	if (0 < n&&n < 100)
	{
		for (int i = 1; i <= n; i++)
		{
			if (i % 10 != 7 && i / 10 != 7 && i % 7 != 0)
			{
				sum += i*i;
			}
		}
		cout << sum;
	}
	else
	{
		cout << "输入错误";
	}
	system("pause");
	return 0;

}
```





## **基础编程练习2**

### 1:求平均年龄

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int n = 0;
	float sum = 0,age,avg = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> age;
		sum += age;
	}
	avg = sum / n;
	printf("%.2lf\n", avg);

	system("pause");
	return 0;

}
```



### 2:计算书费

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int  k = 0;
	float price[10];
	cin >> k;
	for (int i = 0; i < k; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			cin >> price[j];
		}
		printf("%.2lf\n", 28.9*price[0] + 32.7*price[1] + 45.6 *price[2]
			  + 78 * price[3] + 35 * price[4] + 86.2*price[5] + 27.8*price[6] + 43 * price[7] + 56 * price[8] + 65 * price[9]);
	}


	system("pause");
	return 0;

}
```



### 3:计算三角形面积

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	float point[6];
	for (int i = 0; i < 6; i++)
	{
		cin >> point[i];
	}
	float a, b,c;
	a = sqrt(powf(point[0] - point[2], 2) + powf(point[1] - point[3], 2));
	b = sqrt(powf(point[0] - point[4], 2) + powf(point[1] - point[5], 2));
	c = sqrt(powf(point[2] - point[4], 2) + powf(point[3] - point[5], 2));

	float p = (a + b + c) / 2;

	printf("%.2f\n", sqrt(p*(p - a)*(p - b)*(p - c)));


	system("pause");
	return 0;

}
```





### 4:骑车与走路

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int dis;
		cin >> dis;
		if (dis>100)
			cout << "Bike" << endl;
		else if (dis == 100)
			cout << "All" << endl;
		else
			cout << "Walk" << endl;
	}

	system("pause");
	return 0;

}
```



### 5:点和正方形的关系 

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int a, b;
	while (cin >> a >> b)
	{
		if (-1 <= a &&a <= 1 && -1 <= b&&b <= 1)
			cout << "yes" << endl;
		else
			cout << "no" << endl;
	}
	

	system("pause");
	return 0;

}
```



### 6:数组逆序重放

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int n = 0;
	cin >> n;
	int a[1001];
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
	for (int i =n-1; i>=0; i--)
	{
		cout << a[i]<<" ";
	}
	system("pause");
	return 0;

}
```



### 7:整数的个数

```c++

#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int k = 0;
	cin >> k;
	int num,one = 0,five = 0,ten = 0;
	for (int i = 0; i < k; i++)
	{
		cin >> num;
		if (num == 1)
			one += 1;
		else if (num == 5)
			five += 1;
		else if (num == 10)
			ten += 1;

	}
	cout << one << endl << five << endl << ten << endl;

	system("pause");
	return 0;

}
```





### 8:1的个数

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int n = 0;
	cin >> n;
	int num;
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		int temp = 0;
		while (num>0)
		{
			if (num % 2 == 0)
				num /= 2;
			else
			{
				num /= 2;
				temp += 1;
			}
		}
		cout << temp << endl;
	}

	system("pause");
	return 0;

}
```



## **基础编程练习（数据成分）**

### 1:短信计费

```c++

#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int n = 0;
	cin >> n;
	int num,total = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		if (num%70==0)
			total += (num / 70);
		else
			total += (num / 70 + 1);
	}
	printf("%.1f", total*0.1);
	system("pause");
	return 0;

}
```



### 2:奥运奖牌计数

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{
	int n; cin >> n;
	int a = 0, b = 0, c = 0, tmp;
	while (n--)
	{
		cin >> tmp; a += tmp;
		cin >> tmp; b += tmp;
		cin >> tmp; c += tmp;
	}
	cout << a << " " << b << " " << c << " " << a + b + c << endl;


	system("pause");
	return 0;

}
```



### 3:整数的个数

略

### 4:整数奇偶排序

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{

	int a[10];
	int b[10];
	while (cin >> a[0] >> a[1] >> a[2] >> a[3] >> a[4] >> a[5] >> a[6] >> a[7] >> a[8] >> a[9])
	{
		int i, j, cnt1, cnt2;
		cnt1 = 0;
		cnt2 = 9;
		for (i = 0; i<10; i++)
		{
			if (a[i] % 2 != 0)
				b[cnt1++] = a[i];
			else
				b[cnt2--] = a[i];
		}

		for (i = 0; i<cnt1 - 1; i++)
		{
			for (j = i + 1; j<cnt1; j++)
			{
				if (b[i]<b[j])
					swap(b[i], b[j]);
			}
		}

		for (i = cnt1; i<9; i++)
		{
			for (j = i + 1; j<10; j++)
			{
				if (b[i]>b[j])
					swap(b[i], b[j]);
			}
		}
		for (i = 0; i<10; i++)
			cout << b[i] << " ";
		cout << endl;
	}


	system("pause");
	return 0;

}
```



### 5:细菌的战争

```c++
#include<iostream>
#include<math.h>
using namespace std;


int main()
{

	int N = 0, bad = 0, good = 0;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> bad >> good;
		int	hour;
		for (hour = 0;; hour++)
		{
			if (bad <= 0)
			{
				break;
			}
			else
			{
				bad -= good;
				bad = bad << 1;
				good *= 1.05;
				if (bad>1000000)
				{
					bad = 1000000;
				}
			}
		}
		cout << hour << endl;
	}


	system("pause");
	return 0;

}
```



### 6:能被3，5，7整除的数

```c++
#include <iostream>
#include <math.h>
using namespace std;

int main()
{	
	int n;
	while (cin >> n)
	{
		int i = 0;
		if (n % 3 == 0 )
		{
			i += 1;
		}
		if (n % 5 == 0)
		{  
			i += 2;
		}
		if (n % 7 == 0)
		{
			i += 4;
		}
		switch (i)
		{	
			case 0:cout << "n"<<endl; break;
			case 1:cout << "3" << endl; break;
			case 2:cout << "5" << endl; break;
			case 3:cout << "3 5" << endl; break;
			case 4:cout << "7" << endl; break;
			case 5:cout << "3 7" << endl; break; 
			case 6:cout << "5 7" << endl; break;
			case 7:cout << "3 5 7" << endl; break;

		default:
			break;
		}
	}

	return 0;
}
```



### 7:谁考了第k名

```c++
#include<iostream>
#include<algorithm>
using namespace std;
struct student {
	int id;
	double score;
} s[101];
int n, k;

int cmp(student A, student B) {
	return A.score > B.score;
}

int main() {
	cin >> n >> k;
	for(int i = 1; i <= n; i++)
		cin >> s[i].id >> s[i].score;
	sort(s + 1, s + 1 + n, cmp);
	cout << s[k].id << " " << s[k].score <<endl;
	return 0;
}
```

```c++
#include<cstdlib>

#include<iostream>
#include<math.h>
using namespace std;



int main()
{
	int N = 0, K = 0;
	int input[100] = { 0 };
	float data[100] = {0};
	cin >> N >> K;
	for (int i = 0; i < N; i++)
	{
		cin >> input[i] >> data[i];
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N - i-1; j++)
		{
			if (data[j] < data[j + 1])
			{
				float t;
				t = data[j];
				data[j] = data[j + 1];
				data[j + 1] = t;
				int m = input[j];
				input[j] = input[j + 1];
				input[j + 1] = m;
			}
		}
	}
	printf("%d %g\n", input[K - 1], data[K - 1]);

	system("pause");
	return 0;

}
```



##  基础编程练习（运算成分）

### 01:鸡尾酒疗法





















