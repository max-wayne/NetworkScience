clear; clc;
load('./A.mat'); beta=0.1:0.1:1;
Pinf=zeros(length(beta),100);
for i=1:length(beta)
    disp(i);
    for j=1:100
        [~, activeNodes]=SIR_model(A,beta(i));
        Pinf(i,j)=length(activeNodes);
    end
end

figure;
plot(beta,mean(Pinf,2),'-o');

function [traceList,activeNodes] = SIR_model(A,beta)
% A: the network, beta: transmission rate.
% traceList: A-->B, activeNodes: A, B.
seed=randi(length(A));  % ���ѡ��һ���ڵ㿪ʼ����
traceList=[];  % ��¼��Ϣ�����켣
activeNodes=seed;  % ��¼������Ľڵ�
candNodes=seed;
while ~isempty(candNodes)       
    rnd = randi(length(candNodes));
    currNode=candNodes(rnd); 
    neib=find(A(currNode,:)==1);
    neib=setdiff(neib,activeNodes);  % ÿ��ֻ���Լ����½ڵ�
    if ~isempty(neib)
        rand_vec=rand(1,length(neib)); 
        tempActive=neib(rand_vec<=beta);  % ������Ľڵ�
        if ~isempty(tempActive)
            candNodes=[candNodes tempActive];
            activeNodes=[activeNodes tempActive];
            for i=1:length(tempActive)
                traceList=[traceList; currNode tempActive(i)];   
            end    
        end
    end
    candNodes(rnd)=[];
end
end

