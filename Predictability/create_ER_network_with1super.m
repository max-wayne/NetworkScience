function [A] = create_ER_network_with1super(n, d, r, alpha)
    % n: the size of network£¬d: average degree, r: constant, alpha: influencer
    A = sparse(n, n); cnt = 0;
    while cnt <= n*d/2
        x = ceil(rand*n); y = ceil(rand*n);
        if A(x, y) ~= 1
            A(x, y) = 1; A(y, x) = 1;
            cnt = cnt + 1;
        end
    end
    % add super node
    c = ceil(r*n^alpha);
    a1 = zeros(1, n);
    rnd = randperm(n);
    a1(rnd(1:c)) = 1;
    A(1, :) = a1; A(: ,1) = a1¡®;
end
