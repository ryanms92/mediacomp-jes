set classpath=".\jars\jython.jar;.\jars\jmf.jar;.\jars\jl1.0.jar;.\jars\junit.jar;.\Sources"
java -version:1.5+ -Dpython.home="jython-2.2.1" -Xmx512m -classpath %classpath% JESstartup


IF NOT %ERRORLEVEL%==0 (
	set java="win-jre\bin\java.exe"


	%java% -Dpython.home="jython-2.2.1" -Xmx512m -classpath %classpath% JESstartup


)