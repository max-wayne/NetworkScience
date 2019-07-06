function [A, degreeList] = configuration_network_by_cumPk(cum_pk,n_node)
% generate network A by configuration model by cumulative distribution of degree

T = 1e3;

flag = 1;
while flag
    while 1
        degreeList = zeros(1,n_node);
        for node = 1:n_node
            p = rand();
            k = find(cum_pk>=p,1,'first');
            degreeList(node) = k;
        end
        sum_k = sum(degreeList);
        if mod(sum_k,2) == 0
            break;
        end
    end
    % generating degree of each node
    disp('gen degree done...');
    disp(sum(degreeList)); disp(max(degreeList));
    
    %initializating the halfLink list and network
    halfLink = zeros(1,sum_k);
    sum_k_now = 0;
    for node = 1:n_node
        halfLink(sum_k_now + 1: sum_k_now + degreeList(node)) = node;
        sum_k_now = sum_k_now +  degreeList(node);
    end
    A = sparse(n_node,n_node);

    flag = 0;
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
            length(halfLink)
            break;
        end
    end
end

