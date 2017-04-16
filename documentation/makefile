dependencies:
	sudo apt-get install unzip && \
	wget http://www.umlet.com/umlet_14_2/umlet-standalone-14.2.zip && \
	unzip umlet-standalone-14.2.zip;

images:
	java -jar Umlet/umlet.jar -action=convert -format=pdf -filename=component_diagram.uxf -output=component_diagram.pdf;
