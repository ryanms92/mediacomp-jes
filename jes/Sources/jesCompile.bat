set classpath=".;..\jars\jython.jar;..\jars\jmf.jar;..\jars\jl1.0.jar;..\jars\junit.jar;..\jars\customizer.jar;..\jars\mediaplayer.jar;..\jars\multiplayer.jar"

javac -target 1.6 *.java -cp %classpath% 
javadoc *.java -d javadoc
