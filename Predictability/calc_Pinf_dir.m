function [GSCC, S_GSCC, GOUT, S_GOUT] = Calc_Pinf_dir(A)
% GSCC:第一大强联通集团 S_GSCC:第二大强连通集团
% GOUT:第一大连通集团 S_GOUT:第二大连通集团
[~, C] = graphconncomp(A); T = tabulate(C); 
gscc_len = sort(T(:, 2));
if length(gscc_len) == length(A)  % 所有点全都不连通
    GSCC = 1; S_GSCC = 1;
    GOUT = 1; S_GOUT = 1;
else
    GSCC = gscc_len(end);
    S_GSCC = gscc_len(find(gscc_len~=gscc_len(end), 1, 'last'));
    cand_cc = gscc_len(find(gscc_len==S_GSCC, 1, 'first'):end);
    gout = [];
    for i = 1 : length(cand_cc)
        big_id = find(T(:, 2)==cand_cc(i));
        for j = 1 : length(big_id)
            temp_id = find(C==big_id(j));
            [temp_len, ~] = calc_gout(A, temp_id);
            gout = [gout temp_len];
        end
    end
    gout = sort(gout);
    GOUT = gout(end); S_GOUT = gout(end-1);
end
end

function [gout_len, list] = calc_gout(M, id)
    list = id; t1 = 0; t2 = 1;
    while t1 ~= t2
        t1 = length(list);
        for i = 1 : length(list)
            idx = find(M(list(i), :)==1);
            list = [list idx];
        end
        list = unique(list);
        t2 = length(list);
    end
    gout_len = length(list);
end
