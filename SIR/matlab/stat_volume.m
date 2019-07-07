function stat_volume(f)
%% plot all ret_vol.
file = strcat('D:/double_check/info/filename_', f, '.txt');
fid = fopen(file, 'r');
d = 10 * 60; % º‰∏Ù10∑÷÷”
while ~feof(fid)
    s = fgetl(fid);
    p = strcat('D:/double_check/info/', s, '/t');
    load(p); [m, ~] = hist(t, (t(length(t))-t(1))/d);
    vol = m;
    save(strcat('D:/double_check/info/', s, '/vol'), 'vol');
end
fclose(fid);

