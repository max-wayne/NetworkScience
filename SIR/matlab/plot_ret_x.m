function plot_ret_x(f, opt)
%% plot all ret_x.
file = strcat('D:/double_check/info/filename_', f, '.txt');
fid = fopen(file, 'r');
figure(); hold on;
while ~feof(fid)
    s = fgetl(fid);
    p = strcat('D:/double_check/info/', s, '/res');
    load(p); 
    if opt == 1; plot(ret_x1, 'o'); else; plot(ret_x2, 'o'); end
end
fclose(fid);

