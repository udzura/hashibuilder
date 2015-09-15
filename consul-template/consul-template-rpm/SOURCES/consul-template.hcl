consul = "127.0.0.1:8500"
//// May also be specified via the envvar CONSUL_TOKEN
// token = "abcd1234"
retry = "10s"
max_stale = "10m"
log_level = "warn"
pid_file = "/var/run/consul-template.pid"

//// Configuration of SSL
// ssl {
//   enabled = true
//   verify = false
//   cert = "/path/to/client/cert.pem"
//   ca_cert = "/path/to/ca/cert.pem"
// }

//// Add a template
// template {
//   source = "/path/on/disk/to/template"
//   destination = "/path/on/disk/where/template/will/render"
//   command = "optional command to run when the template is updated"
// }

//// Multiple template definitions are supported
// template {
//
// }

// If you want to see datails, check out below:
// https://github.com/hashicorp/consul-template#options
