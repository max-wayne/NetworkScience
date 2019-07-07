clear; clc;
load('./A.mat');
alpha=0.3; theta=0.1:0.1:1; Pinf=zeros(1,10);
parfor i=1:length(theta)
    disp(i);
    for j=1:10
        [activeNodes,~]=LT_model(A,alpha,theta(i));
        Pinf(i,j)=length(activeNodes);
    end
end

figure;
plot(theta, mean(Pinf,2),'-o');

function [activeNodes, activeInit]=LT_model(A,alpha,theta)
% A: the network, alpha: ratio of init active nodes, 
% theta: threshold be actived.
N=length(A);
rand_a=randperm(N); 
activeInit=rand_a(1:ceil(alpha*N));  % 初始化alpha比例的激活节点
candNodes=setdiff(1:N,activeInit);
activeNodes=activeInit;

while 1
    t1=length(candNodes);
    tempNodes=candNodes;
    while ~isempty(tempNodes)
        rnd=randi(length(tempNodes));  
        currNode=tempNodes(rnd);  % 随机选择一个点尝试激活
        friends=find(A(:,currNode)==1);
        if length(intersect(friends,activeNodes))/length(friends)>=theta
            activeNodes=[activeNodes currNode];
            candNodes(candNodes==currNode)=[]; 
        end
        tempNodes(tempNodes==currNode)=[];
    end
    t2=length(candNodes);
    if t1==t2; break; end
end
end


