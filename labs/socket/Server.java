import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;

/**
 * Server
 */
public class Server {
    public final static int PORT = 9999;
    public static void main(String[] args) {
        ServerSocket serverSocket;
        Socket connection;
        try {
            System.out.println("Server is waiting to accept user...");
            serverSocket = new ServerSocket(PORT);
            while (true) {
                connection = serverSocket.accept();
                System.out.println("Accept a client");
                System.out.println(serverSocket);
                connection.close();
                serverSocket.close();
            }
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}