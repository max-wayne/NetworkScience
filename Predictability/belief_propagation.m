function Pinf=aaa(A, beta, iter)
% A: the network  beta: bond percolation  iter: simu times
N=length(A); Pinf=zeros(1,iter); [x,y]=find(A);
for t=1:iter
    M=sparse(N,N);  % M: ���������,ÿ������������������������
    for i=1:length(x)  
        M(x(i),y(i))=rand;
    end
    M=update_M(A,M,beta);  % ����M, �ﵽ��̬
    pinf=calc_Pinf(A,M);  % ����Pinf
    Pinf(t)=pinf/N;
end
end

function M=update_M(A,M,beta)
% A: the network  M: transfer matrix  beta: bond percolation
N=length(A);
for i=1:20  % ��������
    M_new=zeros(N,N);
    for j=1:N
        neib=find(A(:,j)); neib=neib';
        for p=neib
            neib_new=neib(neib~=p);
            temp=1;
            for q=neib_new
                temp=temp*(1-M(q,j));
            end
            M_new(j,p)=beta*(1-temp);  % ���±��ϸ���               
        end
    end
    M=M_new;
end
end

function pinf=calc_Pinf(A,M)
% A: the network  M: transfer matrix
N=length(A);
pinf=0;
for i=1:N
    neib=find(A(:,i));
    temp=1;
    for j=neib'
        temp=temp*(1-M(j,i));
    end
    pinf=pinf+(1-temp);
end
end