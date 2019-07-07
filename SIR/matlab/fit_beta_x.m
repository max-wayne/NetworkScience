function fit_beta_x(f, trunc)
%% fitting y_x = beta_1 + sigma(a*exp(-b*x))
file = strcat('D:/double_check/info/filename_', f, '.txt');
fid = fopen(file, 'r'); para = [];
cnt = 0;
while ~feof(fid)
    cnt = cnt + 1; disp(cnt);
    s = fgetl(fid);
    p = strcat('D:/double_check/info/', s, '/res'); load(p);
    beta_x = beta_x2(1:trunc);
    id = beta_x~=0&~isnan(beta_x)&~isinf(beta_x);
    y = diff(beta_x(id)); x = 1 : length(y);
    [a, b] = fit_a_b(x, y);
    para = [para; [beta_x(1) a b]];
end
fclose(fid);
%% save beta_1 and parameter a, b.
save('D:\double_check\info\stat_results\beta1_a_b_2017_trunc10', 'para');
