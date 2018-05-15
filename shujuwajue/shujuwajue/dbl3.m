function g  = Denclue(iris_D,h_ksin,e_x)
[m,n]=size(iris_x);
ksin;
e=0.0001;
h=1;
d=n;
bandwidth_x=0;
f_x=0;%题目中提到的参数赋初值
x_known={};%已知的x点
y=zeros(1,n);%暂时存放一行数据
x_maximal=zeros(m,n);%x*的值

K_fx=zeros(1,m);%计算fx时用来求和

A=zeros(:,n);%集合A
R=zeros(:,n);%集合R
k=1;%用于计算A\R的行数

for i=1:m
    y(i)=iris(i,:);
    x_maximal(i,:)=FindAttractor(iris(i,:),iris,h,e);
    for j=1:m
        %x_ti(i,:)=(x_known-x(i,:));
        K_fx(j)=K_fx(j-1)+exp( -((x_known-iris_x(j,:))*(x_known-iris_x(j,:)))/(2*h*h) )/sqrt(2*pi);
    end
    f_x=K(t)/(n*h^d);
    if f_x>=ksin
        A(k,:)=x_maximal(i,:);
        R(k,:)=iris_x(i,:);
        k=k+1;
    end
end
g=;
end


while 
        
        