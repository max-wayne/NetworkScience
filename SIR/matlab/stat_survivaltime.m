function stat_survivaltime(f, trunc)
%% stat each info SurvivalTime.
file = strcat('D:/double_check/info/filename_', f, '.txt');
fid = fopen(file, 'r'); T = [];
while ~feof(fid)
    s = fgetl(fid);
    p = strcat('D:/double_check/info/', s, '/vol.mat');
    load(p); vol_cdf = cumsum(vol)/sum(vol);
    k = find(vol_cdf>=trunc, 1, 'first'); t = (10*k)/60; % °´Ð¡Ê±Í³¼Æ
    T = [T; t];
end
fclose(fid);
%% save SurvivalTime
save('D:\double_check\info\stat_results\SurvivalTime', 'T');
