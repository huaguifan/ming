[m,n]=size(iris);
%Lab2_1
%求phai矩阵
array_K=zeros(m,m);
phai_X=zeros(m,n+6);
for i=1:m
    for j=1:n
        phai_X(i,j)=iris(i,j)*iris(i,j);
    end
    for k=n+1:n+3
        phai_X(i,k)=sqrt(2)*iris(i,1)*iris(i,k-n+1);
    end
    for k=n+4:n+5
        phai_X(i,k)=sqrt(2)*iris(i,2)*iris(i,k-n-1);
    end
    phai_X(i,10)=sqrt(2)*iris(i,3)*iris(i,4);
end

%求array_K 二次矩阵
for i=1:m
    for j=1:m
        array_K(i,j)=phai_X(i,:)*(phai_X(j,:).');
    end
end

%求 线性矩阵
linear_K=zeros(m,m);
for i=1:m
    for j=1:m
        linear_K(i,j)=iris(i,:)*(iris(j,:).');
    end
end

%求均值u_phai
u_phai=0;
for i=1:m
    for j=1:m
        u_phai=u_phai+array_K(i,j);
    end
end
u_phai=sqrt(u_phai/(m*m));

for i=m
    %phai_X(i,:)=phai_X(i,:)-u_phai;
end

%求中心
phai_X=phai_X - u_phai;
%求array_n_K，中心矩阵
center_K=zeros(m,m);
for i=1:m
    for j=1:m
        center_K(i,j)=phai_X(i,:)*(phai_X(j,:).');
    end
end
%center_K
%归一化
n_K=zeros(m,m);
final_K=zeros(m,m);
for i=1:m
    for j=1:m
        n_K(i,j)=center_K(i,j)/sqrt(center_K(i,i)*center_K(j,j));
    end
end

%求第三问的点积
for i=1:m
    for j=1:m
        final_K(i,j)=dot(n_K(i,:),n_K(j,:));
    end
end
%验证结果
a=1;
if(final_K==array_K)
    a
end
final_K
%array_K
%n_K