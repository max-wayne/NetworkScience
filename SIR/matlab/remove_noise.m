function remove_noise()
clear; clc;
file = strcat('D:/double_check/info/filename_2017.txt');
data_path = 'D:/double_check/info/';
fid = fopen(file, 'r');
cnt = 0; interim_res_fenmu = zeros(337, 200); interim_res_fenzi = zeros(337, 200);
while ~feof(fid)
    cnt = cnt + 1; disp(cnt);
    s = fgetl(fid);
    load(strcat(data_path, s, '/see_dict.txt')); load(strcat(data_path, s, '/ret_dict.txt'));
    beta_x_clean = []; signal = length(see_dict(:, 2)==1) * 0.01;
    for i = 1 : 200
        u1 = see_dict(see_dict(:, 2)>=i, 1);
        u2 = ret_dict(ret_dict(:, 2)<i, 1);
        u3 = setdiff(u1, u2); u4 = ret_dict(ret_dict(:, 2)==i, 1);
        interim_res_fenmu(cnt, i) = length(u3);
        interim_res_fenzi(cnt, i) = length(intersect(u3, u4));
    end
end
fclose(fid);
%% save
save('D:\double_check\info\stat_results\interim_res', 'interim_res_fenmu', 'interim_res_fenzi');



