CORPUS ?= ./corpus
RM_SHARP_COMMENT = sed -i '' '/^ *\#/d' {} \;
# see http://bbs.linuxpk.com/thread-35972-1-1.html
RM_C_COMMENT = sed -i '' 's/\/\*.*\*\///; /\/\*/,/\*\//d; s/ \/\/.*//' {} \;
RM_SQL_COMMENT = sed -i '' '/^ *--/d' {} \;

.PHONY: clean_comments

clean_comments:\
	clean_config_comments\
	clean_script_comments\
	clean_c_comments\
	clean_sql_comments

clean_config_comments:
	find $(CORPUS) -iname '*.conf' -exec $(RM_SHARP_COMMENT)

clean_script_comments:
	find $(CORPUS) -iname '*.script!' -exec $(RM_SHARP_COMMENT)
	find $(CORPUS) -iname '*.py' -exec $(RM_SHARP_COMMENT)
	find $(CORPUS) -iname '*.rb' -exec $(RM_SHARP_COMMENT)

clean_c_comments:
	find $(CORPUS) -iname '*.c' -exec $(RM_C_COMMENT)
	find $(CORPUS) -iname '*.h' -exec $(RM_C_COMMENT)
	find $(CORPUS) -iname '*.cpp' -exec $(RM_C_COMMENT)
	find $(CORPUS) -iname '*.java' -exec $(RM_C_COMMENT)

clean_sql_comments:
	find $(CORPUS) -iname '*.sql' -exec $(RM_SQL_COMMENT)

