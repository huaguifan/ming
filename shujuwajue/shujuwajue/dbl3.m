function g  = Denclue(iris_D,h_ksin,e_x)
[m,n]=size(iris_x);
ksin;
e=0.0001;
h=1;
d=n;
bandwidth_x=0;
f_x=0;%��Ŀ���ᵽ�Ĳ�������ֵ
x_known={};%��֪��x��
y=zeros(1,n);%��ʱ���һ������
x_maximal=zeros(m,n);%x*��ֵ

K_fx=zeros(1,m);%����fxʱ�������

A=zeros(:,n);%����A
R=zeros(:,n);%����R
k=1;%���ڼ���A\R������

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
        
        