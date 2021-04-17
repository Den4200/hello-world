(import "$.webserver" :all)

(server 
  [
    [:get "/" (
      fun [request]
      [:html
        [
          [:h1 "Hello,"]
          [:h2 "world!"]
        ]])]]
  
  "0.0.0.0" 9999)
