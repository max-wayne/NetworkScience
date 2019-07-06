function gen_sf_undir_XIE(n, k_min, k_max, gamma, output_f)
    % n:网络规模，k_min:最小度，k_max:最大度，gamma:标度律
    k = k_min : k_max;
    p_k_he = sum(k.^(-gamma)); p_k = k.^(-gamma)./p_k_he;
    cum_pk = cumsum(p_k); cum_pk = [zeros(1, k_min-1) cum_pk];
    [A, degreeList] = configuration_network_by_cumPk(cum_pk, n);
    save(strcat(output_f, '\A'), 'A');
    save(strcat(output_f, '\degreeList'), 'degreeList');
end
