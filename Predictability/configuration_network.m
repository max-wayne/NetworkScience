function A = configuration_network(degreeList)
% generate network A by configuration model
% sum k = even should be checked before calling this function
% degreeList : degree of each node in the network

T = 1e5;
%initializating
n_node = length(degreeList);
sum_k = sum(degreeList);

flag = 1;
while flag == 1
    flag = 0;
    %initializating the halfLink list and network
    halfLink = zeros(1,sum_k);
    sum_k_now = 0;
    for node = 1:n_node
        halfLink(sum_k_now + 1: sum_k_now + degreeList(node)) = node;
        sum_k_now = sum_k_now +  degreeList(node);
    end
    A = sparse(n_node,n_node);

    while isempty(halfLink) == 0
        try_time = 0;
        while try_time < T
            s_id = unidrnd(length(halfLink));
            s = halfLink(s_id);
            t_id = unidrnd(length(halfLink));
            t = halfLink(t_id);
            if (s~=t) && (A(s,t)==0)
                A(s,t)=1;
                A(t,s)=1;
                halfLink([s_id,t_id])=[];
                break
            end
            try_time = try_time + 1;
        end
        if try_time >= T
            flag = 1;
            break;
        end
    end
end

