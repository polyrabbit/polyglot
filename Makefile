CORPUS ?= ./corpus
RM_SHARP_COMMENT = sed '/^ *\#/d' {} \;

.PHONY: clean_comments

clean_comments: clean_config_comments clean_script_comments

clean_config_comments:
	echo $(RM_SHARP_COMMENT)
	find $(CORPUS) -name '*.conf' -exec $(RM_SHARP_COMMENT)

clean_script_comments:
	find $(CORPUS) -name '*.script!' -exec $(RM_SHARP_COMMENT)
	find $(CORPUS) -name '*.py' -exec $(RM_SHARP_COMMENT)
	find $(CORPUS) -name '*.rb' -exec $(RM_SHARP_COMMENT)
