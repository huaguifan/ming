function f  = FindAttractor(x,iris_D,h_x,e_x)
[m,n]=size(iris_D);
%x=zeros(m,n);    
x_ti=zeros(m,n);  
K=zeros(m); 
K_x=zeros(m,n); 
t=0;    
x(t,:)=x;
mode_x=0;
while mode_x>e_x
    for i=1:m
        x_ti(i,:)=0;
        x_ti(i,:)=(x(t,:)-x(i,:));
        K_x(t,:)=K_x(t-1,:)+x(t,:)*exp( -(x_ti(i,:)*x_ti(i,:))/(2*h_x*h_x) )/sqrt(2*pi);
        K(t)=K_x(t-1,:)+exp( -(x_ti(i,:)*x_ti(i,:))/(2*h*h) )/sqrt(2*pi);
    end
    x(t+1,:)=K_x(t,:)/K(t);
    mode_x=mode(x(t,:)-x(t-1,:));
    t=t+1;
end     
f=x(t,:);
end