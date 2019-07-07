function plot_ret_cnt(f, d)
%% plot all ret_cnt.
file = strcat('D:/double_check/info/filename_', f, '.txt');
fid = fopen(file, 'r'); ret_cnt = [];
figure(); hold on;
while ~feof(fid)
    s = fgetl(fid);
    p = strcat('D:/double_check/info/', s, '/res');
    load(p); trunc = length(t3(:, 3));
    if trunc >= d
        a = t3(1:d, 3)./100; 
    else
        a = t3(:, 3); a(trunc+1 : d) = 0; a = a./100;
    end
    ret_cnt = [ret_cnt; a'];
end
fclose(fid);
%%
x = 1 : d;
bar(x, mean(ret_cnt));

