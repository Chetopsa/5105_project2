# create a zip file excluding non-source files

ZIP_NAME=5105_Project_2.zip
SOURCE_DIR=.

zip:
	@echo "Creating zip file $(ZIP_NAME) excluding non-source files..."
	@find $(SOURCE_DIR) \
		-not -path "*/__pycache__/*" \
		-not -name ".DS_Store" \
		-type f | zip -@ $(ZIP_NAME)

.PHONY: zip