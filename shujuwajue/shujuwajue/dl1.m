%Lab1-1
[m,n]=size(test);%获取test大小
mean=mean(test);
cov(mean);
%Lab1-2
remean=zeros(m,n);
%中心矩阵
for i=1:m
    remean(i,:)=test(i,:)-mean;
end

E=remean'*remean/m;

%Lab1-3
s=zeros(10,10);
for i=1:m
    d=remean(i,:);
    s=s+d'*d;
end
E2=s/m;


%Lab1-4
%计算Z1
X1=remean(:,1);
Z1=sqrtm(X1.'*X1);
m1=X1/Z1;
%计算Z2
X2=remean(:,2);
Z2=sqrtm(X2.'*X2);
m2=X2/Z2;
relation=m1'*m2;

d=1:m;
plot(d,test(:,1),'.','MarkerSize',5,'Color','r');
plot(d,test(:,2),'.','MarkerSize',5,'Color','b');



%Lab1-5     
x=test(:,1)';
%均值
mu=mean(x);
%方差
s=var(x);
%mux=(zeros(m,1)+1)*mu;%扩展

xx=min(x):0.1:max(x);
figure
plot(xx,normpdf(xx,mu,s));
%-------------------------------------
%x=test(:,1)';
%均值
%mu=mean(x);
%方差
%s=var(x);
%mux=(zeros(m,1)+1)*mu;%扩展

%xx=min(x):0.1:max(x);
%figure
%plot(xx,normpdf(xx,mu,s));

%Lab1-6
var(test);
%Lab1-7
test_x=cov(test);
max(max(test_x))
[i,j]=find(test_x==max(max(test_x)));
i
j
max(min(test_x));
[p2,q2]=find(test_x==min(min(test_x)));
p2 
q2














