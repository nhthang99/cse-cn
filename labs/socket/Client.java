import java.io.IOException;
import java.net.Socket;
import java.net.SocketException;
import java.net.UnknownHostException;

/**
 * Client
 */
public class Client {

    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 9999);
            System.out.println("Connected to "
                + socket.getInetAddress() +" on port "
                + socket.getPort() + " from port "
                + socket.getLocalPort() + " of "
                + socket.getLocalAddress());
            socket.close();
        } catch (UnknownHostException e) {
            System.out.println(e);
        } catch (SocketException e) {
            System.out.println(e);
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}