package main

import (
	"fmt"
	"log"
	"net/http"
)

// Router function to handle different routes
func setupRouter() *http.ServeMux {
	// Create a new ServeMux (multiplexer)
	mux := http.NewServeMux()

	// Home route handler
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/" {
			http.NotFound(w, r)
			return
		}
		fmt.Fprintln(w, "Welcome to the Home Page!")
	})

	// Users route handler
	mux.HandleFunc("/users", func(w http.ResponseWriter, r *http.Request) {
		switch r.Method {
		case http.MethodGet:
			fmt.Fprintln(w, "List all users")
		case http.MethodPost:
			fmt.Fprintln(w, "Create a new user")
		default:
			http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		}
	})

	// User details route handler
	mux.HandleFunc("/users/", func(w http.ResponseWriter, r *http.Request) {
		// Extract user ID from the URL
		userID := r.URL.Path[len("/users/"):]
		
		switch r.Method {
		case http.MethodGet:
			fmt.Fprintf(w, "Get details for user %s", userID)
		case http.MethodPut:
			fmt.Fprintf(w, "Update user %s", userID)
		case http.MethodDelete:
			fmt.Fprintf(w, "Delete user %s", userID)
		default:
			http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		}
	})

	return mux
}

func main() {
	// Setup the router
	router := setupRouter()

	// Start the server
	port := ":8080"
	fmt.Printf("Server starting on port %s\n", port)
	log.Fatal(http.ListenAndServe(port, router))
}