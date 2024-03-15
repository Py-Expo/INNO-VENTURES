<?php
        // Database configuration
        $servername = "localhost"; // Replace with your MySQL server hostname
        $username = "your_username"; // Replace with your MySQL username
        $password = "your_password"; // Replace with your MySQL password
        $database = "bmi_calculator_db"; // Replace with your MySQL database name

        // Create connection
        $conn = new mysqli($servername, $username, $password, $database);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Fetch data from the database
        $sql = "SELECT * FROM bmi_results";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            // Output data of each row
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $row["id"] . "</td>";
                echo "<td>" . $row["height"] . "</td>";
                echo "<td>" . $row["weight"] . "</td>";
                echo "<td>" . $row["age"] . "</td>";
                echo "<td>" . $row["sex"] . "</td>";
                echo "<td>" . $row["bmi"] . "</td>";
                echo "<td>" . $row["created_at"] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "0 results";
        }

        // Close connection
        $conn->close();
        ?>