Create DataBase: user_table(id, uid, fos, fas), fo_table(id, fo), fa_table(id, fa)
Steps:
    1. Discrete user_id, form User_Dict.txt rather than .json. Because the latter consume more memory;
       The User_Dict.txt format is: uid   id
    2. Create User_TABLE(id uid) and set id as primary key;
    3. Use the User_Dict.txt and the original follow_file to create NEW follower_TXT;
       The NEW follower_TXT's format is: id     follower1   follower2   ...
    4. Create Fo_TABLE(id follower...) using the NEW follower_TXT and set id as primary key;
    5. Reverse follower_file and get fan_TXT. There are some skills: because of the follower_file is so large that the memory can
       not load the fan_dict, so we just form a relatively small fan_TXT, say the user_id form 1 to 10000000, for one traversal;
    6. Create Fa_TABLE(id fans...) using fan_TXTs. To save time, there should not have query operation, just insert;
    7. Count the number of followers and fans of every user;
    8. ExtractRestUser and CreateRestDB function deal with the rest users.
    9. Just extract the needed(ExtractRestUser-->CreateRestFan-->CreateRestDB)
